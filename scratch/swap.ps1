$content = Get-Content -Raw -Path index.html

# We will use Regex to capture the blocks. 
# Project 02: starts with <!-- PROJECT 02 — SMI SUPERMARKETS --> and ends right before <!-- PROJECT 03 — PUBLIC SECTOR UX & TRUST -->
# Project 06: starts with <!-- PROJECT 06 — KILLER GLUTE BIKES BI (full width) --> and ends right before </div><!-- /projects-grid -->

$regex = '(?s)(<!-- PROJECT 02 — SMI SUPERMARKETS -->.*?)(?=<!-- PROJECT 03 — PUBLIC SECTOR UX & TRUST -->)'
if ($content -match $regex) {
    $p2Block = $matches[1]
}

$regex6 = '(?s)(<!-- PROJECT 06 — KILLER GLUTE BIKES BI \(full width\) -->.*?)(?=\s*</div><!-- /projects-grid -->)'
if ($content -match $regex6) {
    $p6Block = $matches[1]
}

if ($p2Block -and $p6Block) {
    Write-Host "Found both blocks."
    
    # Process P6 to become P2
    $newP2 = $p6Block -replace 'PROJECT 06', 'PROJECT 02'
    $newP2 = $newP2 -replace '<span class="proj-num">06</span>', '<span class="proj-num">02</span>'
    $newP2 = $newP2 -replace ' project-card--full', ''
    $newP2 = $newP2 -replace '\(full width\)', ''
    
    # Process P2 to become P6
    $newP6 = $p2Block -replace 'PROJECT 02', 'PROJECT 06'
    $newP6 = $newP6 -replace '<span class="proj-num">02</span>', '<span class="proj-num">06</span>'
    $newP6 = $newP6 -replace 'class="card project-card"', 'class="card project-card project-card--full"'
    $newP6 = $newP6 -replace 'PROJECT 06 — SMI SUPERMARKETS', 'PROJECT 06 — SMI SUPERMARKETS (full width)'
    
    # Replace in content
    $content = $content.Replace($p2Block, "%%TEMP_P2%%")
    $content = $content.Replace($p6Block, $newP6)
    $content = $content.Replace("%%TEMP_P2%%", $newP2)
    
    Set-Content -Path index.html -Value $content -Encoding UTF8
    Write-Host "Swap completed successfully."
} else {
    Write-Host "Could not find one or both blocks."
}
